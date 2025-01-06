# �klid mesafesini hesaplayan fonksiyon
def euclidean_distance(x1, y1, x2, y2):
    # Ad�m 1: x ve y farklar�n� hesapla
    x_diff = x2 - x1
    y_diff = y2 - y1

    # Ad�m 2: Farklar�n karelerini hesapla
    x_diff_squared = x_diff * x_diff
    y_diff_squared = y_diff * y_diff

    # Ad�m 3: Karelerin toplam�n� hesapla
    sum_of_squares = x_diff_squared + y_diff_squared

    # Ad�m 4: Toplam�n karek�k�n� al
    distance = sum_of_squares ** 0.5

    return distance

# Noktalar�n tan�mlanmas�
points = [(1, 2), (4, 6), (7, 1), (3, 5)]

# Mesafelerin hesaplanmas�
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        # Nokta �iftlerini al
        point1 = points[i]
        point2 = points[j]

        # Mesafeyi hesapla
        distance = euclidean_distance(point1[0], point1[1], point2[0], point2[1])

        # Mesafeyi listeye ekle
        distances.append(distance)

# Minimum mesafenin bulunmas�
if len(distances) > 0:
    min_distance = distances[0]
    for distance in distances:
        if distance < min_distance:
            min_distance = distance
else:
    min_distance = None

# Sonu�lar� yazd�rma
print("T�m mesafeler:", distances)
if min_distance is not None:
    print("En k���k mesafe:", min_distance)
else:
    print("Mesafe hesaplanamad�.")

