---
title: FileFilter
publishDate: 2024-11-20 00:00:00
img: /assets/filefilter-cover.png
img_alt: A clean interface showing image filtering options
description: |
  Desktop image processing tool with batch operations,
  smart filtering, and format conversion powered by OpenCV.
tags:
  - Dev
  - Python
  - Desktop
---

FileFilter is a desktop tool for batch image processing and file management. Built with Python and OpenCV, it streamlines repetitive image operations like resizing, format conversion, filtering, and organizing files by metadata.

## Key Features

- **Batch image processing** — resize, crop, and convert hundreds of images at once
- **Smart filtering** by resolution, file size, format, and EXIF metadata
- **Format conversion** between PNG, JPEG, WebP, TIFF, and more
- **Duplicate detection** using perceptual hashing to find similar images
- **Custom filter pipelines** — chain operations together for complex workflows

## Tech Stack

- **Core**: Python, OpenCV, Pillow
- **UI**: Desktop GUI with drag-and-drop support
- **Processing**: Multi-threaded batch operations for speed
- **Detection**: Perceptual hashing, EXIF parsing
