#Öncelikle indirilimesi gerekmektedir.
#cmd ->pip install -U googlemaps

import googlemaps
from datetime import datetime

# Google Maps API anahtarınızı buraya yapıştırın
gmaps = googlemaps.Client(key='YOUR_API_KEY')#Kullanıcıya göre değişiklik gösterecek

def find_places(location, radius, keyword):
    """
    Belirli bir konum etrafındaki belirli bir yarıçapta yerleri bulur.
    """
    places = gmaps.places_nearby(location=location, radius=radius, keyword=keyword)
    return places['results']

def main():
    # Kullanıcıdan konum bilgisi alınabilir veya sabit bir konum kullanılabilir.
    location = (40.7128, -74.0060)  # Örnek: New York City'nin koordinatları

    radius = 5000  # Metre cinsinden yarıçap (örneğin, 5 km)

    # Kadınlar ve kız çocukları için önemli yerlerin anahtar kelimeleri
    keywords = ['women support center', 'healthcare', 'safe gathering place']

    for keyword in keywords:
        places = find_places(location, radius, keyword)
        print(f"Yerler \"{keyword}\" anahtar kelimesine göre bulundu:")
        for place in places:
            print(place['name'], place['vicinity'])

if __name__ == "__main__":
    main()
