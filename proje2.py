import requests

def find_safe_places(api_key, location, radius=5000):
    """
    Kadınlar ve kız çocukları için güvenli yerleri bulan fonksiyon.
    
    Args:
        api_key (str): Google Places API anahtarı.
        location (str): Arama yapılacak konum (örneğin, "İstanbul, Türkiye").
        radius (int): Arama yarıçapı, varsayılan olarak 5000 metre.
        
    Returns:
        list: Güvenli yerlerin bir listesi (ad, adres ve tür bilgisi içerir).
    """
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "key": api_key,
        "location": location,
        "radius": radius,
        "keyword": "support center|health center|safe space for women and children",
        "language": "tr"  # Türkçe sonuçlar için dil seçeneği
    }
    
    response = requests.get(url, params=params)
    results = response.json().get("results", [])
    
    safe_places = []
    for place in results:
        place_name = place.get("name")
        place_address = place.get("vicinity")
        place_types = place.get("types", [])
        safe_places.append({
            "name": place_name,
            "address": place_address,
            "types": place_types
        })
    
    return safe_places

def main():
    api_key = "YOUR_GOOGLE_MAPS_API_KEY"
    location = "İstanbul, Türkiye"  # Arama yapılacak konum
    radius = 10000  # Arama yarıçapı (metre cinsinden)
    
    safe_places = find_safe_places(api_key, location, radius)
    
    print("Güvenli yerler:")
    for place in safe_places:
        print(f"Ad: {place['name']}, Adres: {place['address']}, Türler: {place['types']}")

if __name__ == "__main__":
    main()
