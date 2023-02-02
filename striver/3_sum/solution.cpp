class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> ans;
        int n = nums.size();
        sort(nums.begin(), nums.end());
        // for(auto x:nums){
        //     cout<<x<<" ";
        // }
        // cout<<endl;
        for(int k = 0; k < n-2; k++){
            if(k>0 && nums[k] == nums[k-1]) continue;
            int target = nums[k];
            int i = k+1;
            int j = n-1;
            // cout<<target<<": ";
            while(i<j){
                int sum = nums[i]+nums[j]+target;
                // cout<<sum<<" ";
                if(sum == 0){
                    ans.push_back({target, nums[i], nums[j]});
                    i++;
                    j--;
                    while(i<j && nums[i-1]==nums[i]) i++;
                    while(i<j && nums[j+1]==nums[j]) j--;
                }else if(sum<0){
                    i++;
                }else{
                    j--;
                }
            }
            // cout<<endl;
        }
        return ans;
    }
};
