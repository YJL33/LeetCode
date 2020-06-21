
import java.util.*;

public class Solution {
    public String[] getFolderNames(String[] names) {
    	String[] res = new String[names.length];
    	Map<String, Integer> output = new HashMap<String, Integer>();
    	for (int i = 0; i < names.length; i++) {
    		if (!output.containsKey(names[i])) {
    			output.put(names[i], 1);
    			res[i] = names[i];
    		}
    		else {
    			int x = output.get(names[i]);
    			String newName = names[i] + "(" + String.valueOf(x) + ")";
    			while (output.containsKey(newName)) {
    				x += 1;
    				newName = names[i] + "(" + String.valueOf(x) + ")";
    			}
    			output.put(names[i], x);
    			output.put(newName, 1);
    			res[i] = newName;
    		}
    	}

    	return res;

    }
    public static void main(String[] args) {
        Solution sol = new Solution();
        String[] input = {"AAA", "BBB"};
        // String[] input = {"5", "-8", "9", "-12", "2", "8", "4", "*", "*", "*", "*", "2", "*", "5"};
        String[] output = sol.getFolderNames(input);
        for (String o : output) {
        	System.out.println(o);
        }
    }
}