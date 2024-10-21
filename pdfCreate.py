from reportlab.lib.pagesizes import landscape, A4
from reportlab.pdfgen import canvas
from reportlab.lib import utils
import os

def add_images_to_pdf(c, image_path, num_images, image_scale):
    """Add images to the PDF, four per page."""
    images_per_page = 2  # Number of images per page
    for i in range(num_images):
        try:
            # Load the image
            img = utils.ImageReader(image_path)
            img_width, img_height = img.getSize()

            # Calculate scaled dimensions
            scaled_width = img_width * image_scale
            scaled_height = img_height * image_scale

            # Calculate x and y positions to center the images
            if i % images_per_page == 0 and i > 0:
                c.showPage()  # Start a new page after every four images

            # Determine the position of the image on the page
            pos = i % images_per_page
            x = (landscape(A4)[0] / 2 - scaled_width) / 2 + (pos % 2) * (landscape(A4)[0] / 2)
            y = (landscape(A4)[1] - scaled_height) / 2 - (pos // 2) * (scaled_height)

            c.drawImage(image_path, x, y, width=scaled_width, height=scaled_height)
        except Exception as e:
            print(f"Error adding image {image_path}: {e}")

def create_large_pdf(file_name, image_path, num_images, image_scale):
    """Create a large PDF with specified parameters."""
    c = canvas.Canvas(file_name, pagesize=landscape(A4))  # Set page size to landscape
    add_images_to_pdf(c, image_path, num_images, image_scale)
    c.save()  # Save the PDF

if __name__ == "__main__":
    output_pdf = "large_pdf_with_images_landscape_centered.pdf"
    image_path = "image.jpg"  # Path to the image file
    
    # PDF parameters
    num_images = 150000  # You can change this number for more images
    image_scale = 0.25   # Scale factor for the images

    create_large_pdf(output_pdf, image_path, num_images, image_scale)

    # Check the size of the generated PDF
    file_size = os.path.getsize(output_pdf) / (1024 * 1024)  # Size in MB
    print(f"Generated PDF size is --> {file_size:.2f} MB")
