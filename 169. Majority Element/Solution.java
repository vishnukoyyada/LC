
class Solution {
    public int majorityElement(int[] nums) {
        Map<Integer, Integer> ans = new HashMap<>();
        
        // Count occurrences of each element
        for (int num : nums) {
            if (ans.containsKey(num)) {
                ans.put(num, ans.get(num) + 1);
            } else {
                ans.put(num, 1);
            }
        }
        
        // Find the element with the maximum count
        int maxi = 0;
        int majorityElement = nums[0];
        for (Map.Entry<Integer, Integer> entry : ans.entrySet()) {
            if (entry.getValue() > maxi) {
                maxi = entry.getValue();
                majorityElement = entry.getKey();
            }
        }
        
        return majorityElement;
    }
}
