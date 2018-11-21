import cv2
from matplotlib import pyplot as plt

def show_picture(imagem):
    while True:
        cv2.imshow("SD", imagem)
        delay = cv2.waitKey(0)

        if delay == 27:
            break
        elif delay == -1:
            continue

def plot_histogram(imagem):
    color = ('r', 'g', 'b')
    for i, col in enumerate(color):
        histr = cv2.calcHist([imagem], [i], None, [256], [0, 256])
        plt.plot(histr, color=col)
        plt.xlim([0, 256])
    plt.show()

def get_histogram(imagem):
    color = ('r', 'g', 'b')

    lista = []

    for i, col in enumerate(color):
        histr = cv2.calcHist([imagem], [i], None, [256], [0, 256])
        lista = lista + histr
    return lista


def get_rgb_pixel(imagem):
    img_shape = imagem.shape
    height = img_shape[0]
    width = img_shape[1]

    vetor = []

    for row in range(width):
        for column in range(height):
            print (imagem[column][row])
    print (vetor)


def main():
    imagem = cv2.imread("madura.jpg")
    show_picture(imagem)
    get_histogram(imagem)
    #lc.limiarizacao_adaptativa(imagem)
    return 0

if __name__ == '__main__':
    main()
