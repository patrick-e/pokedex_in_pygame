from google_images_download import google_images_download

class request_image():
    def __init__(self,nome):
        '''
        pega nomes de pokemon e ira pesquisar no google a imagem
        '''
        self.nome = nome
        

    def image(self):
        response = google_images_download.googleimagesdownload()
        arguments = {"keywords": nome, "limit": 101, "print_urls": True}
        paths = response.download(arguments)
        print(paths)


nome = 'Pikachu'
r = request_image(nome)
r.image()