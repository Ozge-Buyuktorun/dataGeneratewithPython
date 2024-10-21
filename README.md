# Information About PDF Generation

This document explains the process of creating a horizontal PDF file using Python and details the associated code. The code adds a specified image file (e.g., `image.jpg`) multiple times to create a large PDF.

## Libraries Used

- **reportlab**: A Python library used for creating PDF files. In this code, it is used to add images to the PDF and set the page size.
- **os**: A standard Python library used to interact with the file system. In this code, it is used to check the size of the PDF file.

## Code Explanation

### 1. Functions

#### `add_image_to_pdf(c, image_path, num_images, image_scale)`

This function adds the specified image file (`image_path`) to the PDF.

- **Parameters**:
  - `c`: The `canvas` object used to create the PDF.
  - `image_path`: The path of the image file to be added.
  - `num_images`: The number of images to be added to the PDF.
  - `image_scale`: The scaling factor for the image (e.g., `0.12` reduces the image size to 12%).

- **Operation**:
  1. For each image, the scaled width and height are calculated.
  2. The image is placed in the center of the PDF page.
  3. A new page is created after each image is added.

#### `create_large_pdf(file_name, image_path, num_images, image_scale)`

This function creates a PDF file with the specified parameters.

- **Parameters**:
  - `file_name`: The name of the PDF file to be created.
  - `image_path`: The path of the image file to be added.
  - `num_images`: The number of images to be added to the PDF.
  - `image_scale`: The scaling factor for the image.

- **Operation**:
  1. A `canvas` object with a landscape page size is created.
  2. The `add_image_to_pdf` function is called to add images.
  3. The PDF file is saved.

### 2. Main Program

In the main program section, the following operations are performed:

- The output PDF file name (`output_pdf`) and the path of the image to be added (`image_path`) are defined.
- PDF parameters are set:
  - `num_images`: The number of images added to the PDF (e.g., `250000`).
  - `image_scale`: A scaling factor to reduce the image size (e.g., `0.12`).
- The PDF creation function is called.
- The size of the generated PDF file is calculated and printed to the console.

## Usage

1. **Install Required Libraries**:
     ```bash
     pip install reportlab
## Example Output:
- Generated PDF size is --> X.XX MB
