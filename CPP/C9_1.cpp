int find_greatest_common_factor(int M, int N)
{
    int greatest_common_factor(0);
    /// START YOUR CODE HERE ///
    for (int i = M; i >= 1; i--)
    {
        if (M % i == 0)
        {
            if (N % i == 0)
            {
                greatest_common_factor = i;
                break;
            }
        }
        else
        {
            greatest_common_factor = 1;
        }
    }
    return greatest_common_factor;

    //// END YOUR CODE HERE ////
}
