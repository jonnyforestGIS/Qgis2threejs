# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Qgis2threejs
                                 A QGIS plugin
 export terrain data, map canvas image and vector data to web browser
                              -------------------
        begin                : 2014-01-16
        copyright            : (C) 2014 Minoru Akagi
        email                : akaginch@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
import struct

from math import floor
from osgeo import gdal
from PyQt5.QtCore import QSize

from .gdal2threejs import Raster
from .geometry import Point
from .rotatedrect import RotatedRect


class MapTo3D:

  def __init__(self, mapSettings, planeWidth=100, verticalExaggeration=1, verticalShift=0):
    # map canvas
    self.rotation = mapSettings.rotation()
    self.mapExtent = RotatedRect.fromMapSettings(mapSettings)

    # 3d
    canvas_size = mapSettings.outputSize()
    self.planeWidth = planeWidth
    self.planeHeight = planeWidth * canvas_size.height() / canvas_size.width()

    self.verticalExaggeration = verticalExaggeration
    self.verticalShift = verticalShift

    self.multiplier = planeWidth / self.mapExtent.width()
    self.multiplierZ = self.multiplier * verticalExaggeration

  def transform(self, x, y, z=0):
    n = self.mapExtent.normalizePoint(x, y)
    return Point((n.x() - 0.5) * self.planeWidth,
                 (n.y() - 0.5) * self.planeHeight,
                 (z + self.verticalShift) * self.multiplierZ)

  def transformPoint(self, pt):
    return self.transform(pt.x, pt.y, pt.z)


class GDALDEMProvider(Raster):

  def __init__(self, filename, dest_wkt, source_wkt=None):
    Raster.__init__(self, filename)
    self.driver = gdal.GetDriverByName("MEM")
    self.dest_wkt = dest_wkt
    self.source_wkt = source_wkt
    if source_wkt:
      self.ds.SetProjection(str(source_wkt))

  def _read(self, width, height, geotransform):
    # create a memory dataset
    warped_ds = self.driver.Create("", width, height, 1, gdal.GDT_Float32)
    warped_ds.SetProjection(self.dest_wkt)
    warped_ds.SetGeoTransform(geotransform)

    # reproject image
    gdal.ReprojectImage(self.ds, warped_ds, None, None, gdal.GRA_Bilinear)

    # load values into an array
    band = warped_ds.GetRasterBand(1)
    fs = "f" * width * height
    return struct.unpack(fs, band.ReadRaster(0, 0, width, height, buf_type=gdal.GDT_Float32))

  def read(self, width, height, extent):
    return self._read(width, height, extent.geotransform(width, height))

  def readValue(self, x, y):
    """get value at the position using 1px * 1px memory raster"""
    res = 0.1
    geotransform = [x - res / 2, res, 0, y + res / 2, 0, -res]
    return self._read(1, 1, geotransform)[0]

  def readValueOnTriangles(self, x, y, xmin, ymin, xres, yres):
    mx0 = floor((x - xmin) / xres)
    my0 = floor((y - ymin) / yres)
    px0 = xmin + xres * mx0
    py0 = ymin + yres * my0
    geotransform = [px0, xres, 0, py0 + yres, 0, -yres]
    z = self._read(2, 2, geotransform)

    sdx = (x - px0) / xres
    sdy = (y - py0) / yres

    if sdx <= sdy:
      return z[0] + (z[1] - z[0]) * sdx + (z[2] - z[0]) * (1 - sdy)
    return z[3] + (z[2] - z[3]) * (1 - sdx) + (z[1] - z[3]) * sdy


class FlatDEMProvider:

  def __init__(self, value=0):
    self.value = value

  def name(self):
    return "Flat Plane"

  def read(self, width, height, extent):
    return [self.value] * width * height

  def readValue(self, x, y):
    return self.value


def calculateDEMSize(canvasSize, sizeLevel, roughening=0):
  width, height = canvasSize.width(), canvasSize.height()
  size = 100 * sizeLevel
  s = (size * size / (width * height)) ** 0.5
  if s < 1:
    width = int(width * s)
    height = int(height * s)

  if roughening:
    if width % roughening != 0:
      width = int(width / roughening + 0.9) * roughening
    if height % roughening != 0:
      height = int(height / roughening + 0.9) * roughening

  return QSize(width + 1, height + 1)
