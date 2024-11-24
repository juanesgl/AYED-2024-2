from sys import stdin

def read_matrix(h, w):
    matrix = []
    for i in range(h):
        row = list(map(int, stdin.readline().strip().split()))
        matrix.append(row)
    return matrix

def convolve_image(image, kernel, H, W, N, M):
    output_height = H - N + 1
    output_width = W - M + 1
    output = [[0] * output_width for _ in range(output_height)]
#Matriz transpuesta :D
    flipped_kernel = [[kernel[N-1-i][M-1-j] for j in range(M)] for i in range(N)]

    for i in range(output_height):
        for j in range(output_width):
            for k in range(N):
                for l in range(M):
                    output[i][j] += image[i + k][j + l] * flipped_kernel[k][l]

    return output

def main():
    H, W, N, M = map(int, stdin.readline().strip().split())
    
    # Leer la imagen
    image = read_matrix(H, W)
    
    # Leer el kernel
    kernel = read_matrix(N, M)
    
    # Realizar la convolución
    result = convolve_image(image, kernel, H, W, N, M)
    
    # Imprimir la imagen resultante
    for row in result:
        print(" ".join(map(str, row)))

main()