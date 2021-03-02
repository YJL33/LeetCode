
class LCUnitTest {
    public static void main(String[] args) {
        // 535
        String url = "http://cidr.xyz";
        Codec codec = new Codec();
        System.out.println("before:  " + url);
        String encoded = codec.encode(url);
        System.out.println("encoded: " + encoded);
        System.out.println("after:   " + codec.decode(encoded));
    }
}
// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.decode(codec.encode(url));