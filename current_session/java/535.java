import java.util.*;
public class Codec {
    Map<Integer, String> urls = new HashMap<>();
    // Encodes a URL to a shortened URL.
    public String encode(String longUrl) {
        Integer shortened = longUrl.hashCode();
        urls.put(shortened, longUrl);
        return "http://tinyurl.com/"+shortened;
    }

    // Decodes a shortened URL to its original URL.
    public String decode(String shortUrl) {
        return urls.get(Integer.parseInt(shortUrl.replace("http://tinyurl.com/", "")));
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.decode(codec.encode(url));