# Öklid mesafesini hesaplayan fonksiyon
def euclidean_distance(x1, y1, x2, y2):
    # Adým 1: x ve y farklarýný hesapla
    x_diff = x2 - x1
    y_diff = y2 - y1

    # Adým 2: Farklarýn karelerini hesapla
    x_diff_squared = x_diff * x_diff
    y_diff_squared = y_diff * y_diff

    # Adým 3: Karelerin toplamýný hesapla
    sum_of_squares = x_diff_squared + y_diff_squared

    # Adým 4: Toplamýn karekökünü al
    distance = sum_of_squares ** 0.5

    return distance

# Noktalarýn tanýmlanmasý
points = [(1, 2), (4, 6), (7, 1), (3, 5)]

# Mesafelerin hesaplanmasý
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        # Nokta çiftlerini al
        point1 = points[i]
        point2 = points[j]

        # Mesafeyi hesapla
        distance = euclidean_distance(point1[0], point1[1], point2[0], point2[1])

        # Mesafeyi listeye ekle
        distances.append(distance)

# Minimum mesafenin bulunmasý
if len(distances) > 0:
    min_distance = distances[0]
    for distance in distances:
        if distance < min_distance:
            min_distance = distance
else:
    min_distance = None

# Sonuçlarý yazdýrma
print("Tüm mesafeler:", distances)
if min_distance is not None:
    print("En küçük mesafe:", min_distance)
else:
    print("Mesafe hesaplanamadý.")

