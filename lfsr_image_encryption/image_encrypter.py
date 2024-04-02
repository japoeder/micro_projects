# import your LFSR class for use in ImageEncrypter
from lfsr import LFSR
from PIL import Image
import pprint


class ImageEncrypter:

    # initialize an ImageEncrypter object with an LFSR and image file name
    def __init__(self, lfsr: LFSR, file_name: str):
        self.lfsr = lfsr
        self.file_name = file_name
        self.tap = lfsr.tap

    # open the image specified by ‘file_name’ in your constructor
    # you will find the Image.open method useful here
    def open_image(self):
        im_in = Image.open(self.file_name)
        return im_in

    # calls open_image()
    # converts the image to a 2D array of R, G, B triples
    # you will find the Image.load method useful here
    def pixelate(self):
        im_l = ImageEncrypter.open_image(self).load()
        return im_l

    # encrypts the 2D pixelated “image” returned from pixelate()
    # returns the encrypted 2D array
    # you will find the binary XOR operator useful here
    def encrypt(self):

        # Set password equal to LFSR, using input bit string
        pw = self.lfsr.__str__()

        # Load he image so you can grab pixels
        im = ImageEncrypter.pixelate(self)

        # Get dimension of image from open_image object
        im_dim = ImageEncrypter.open_image(self).size
        X = im_dim[0]
        Y = im_dim[1]

        # Create instance of image object for encryption
        im_e = ImageEncrypter.open_image(self)

        # Loop through row index first via vertical axis
        for y in range(X):

            # Loop through column index via horizontal axis
            for x in range(Y):

                # Use x and y coordinates to grab pixel RGB value
                rgb_l = list(im[x, y])

                # Loop through rgb value, encrypt, and update original pixel
                p_l = []
                for c in rgb_l:

                    # Encrypt the pixel color value and append to rgb list
                    ep = bin(c ^ int('0b' + pw, 2))
                    p_l.append(int(ep, 2))

                    # Update password
                    pw = LFSR(pw, self.tap).__str__()

                # Adjust encrypted image object with new RGB values
                im_e.putpixel((x, y), tuple(p_l))

        # Return encrypted image object
        return im_e

    # converts the encrypted 2D pixelated image into an image
    # and names it <file_name>_transform.png
    # you will find the Image.save method useful here
    def save_image(self, file_name: str):
        # your executable code that invokes ImageEncrypter and encrypts/decrypts an # image and saves the result to a
        # file
        ImageEncrypter.encrypt(self).save(file_name)
        return None


def main():
    ImageEncrypter(LFSR('10011010', 5), "N:\\football.png").save_image('N:\\football_transform.png')


if __name__ == "__main__":
    main()
