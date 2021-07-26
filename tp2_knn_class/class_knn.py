class Knn:
    #método construtor e definição de k
    def __init__(self):
        self.k = int(input("Insira valor para k do modelo: "))
        
    def calcular_distancia(self, ponto, data):
        """
        Calculando as distâncias a partir de cada ponto no_class

        """
        self.ponto = ponto
        self.data = data
        
        all_distancias = []
                
        i = 0
        for j in range(len(self.data)):
            dist_1 = self.ponto[2][i] - self.data[j][2][i]
            i+=1
            dist_2 = self.ponto[2][i] - self.data[j][2][i]
            i+=1
            dist_3 = self.ponto[2][i] - self.data[j][2][i]
            i+=1
            dist_4 = self.ponto[2][i] - self.data[j][2][i]
            distancia = (((dist_1**2) + (dist_2**2) + (dist_3**2) + (dist_4**2))**0.5)
            i = 0
            all_distancias.append(distancia)
        return all_distancias
    
    def k_vizinhos(self, all_distancias, k):
        """
        listando vizinhos mais próximos a partir do valor k
        """
        
        self.all_distancias = all_distancias
    
        
        lista_enumerada = (list(enumerate(self.all_distancias)))
        lista_nova = []
        
        
        for i in range(len(lista_enumerada)):
            lista_nova.append(list(lista_enumerada[i]))

        for i in range(len(lista_enumerada)):
            lista_temp = lista_nova[i]
            lista_temp.reverse()
            lista_nova[i] = lista_temp

        lista_nova.sort()
        vizinho = []

        for i in range(self.k):
            vizinho.append(min(lista_nova))
            lista_nova.pop(0)
        return vizinho

    def classifica_no_class(self, vizinho, data, k):
        """
        classificando ponto no_class a partir da moda
        """

        self.vizinho = vizinho
        
        moderado = 0
        conservador = 0
        agressivo = 0

        for i in range(k):
            if data[self.vizinho[i][1]][1] == 'Moderado':
                moderado+=1
            if data[self.vizinho[i][1]][1] == 'Conservador':
                conservador+=1
            if data[self.vizinho[i][1]][1] == 'Agressivo':
                agressivo+=1
        
        if conservador>moderado and conservador>agressivo:
            classicacao = 'Conservador'
        if moderado>conservador and moderado>agressivo:
            classicacao = 'Moderado'
        if agressivo>moderado and agressivo>conservador:
            classicacao = 'Agressivo'
        else:
            classicacao = data[self.vizinho[0][1]][1]

        return classicacao
    