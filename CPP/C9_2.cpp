int find_least_common_multiple(int M, int N)
{
    int least_common_multiple(0);
    /// START YOUR CODE HERE ///
    for (int i = M; i >= 1; i--)
    {
        if (M % i == 0)
        {
            if (N % i == 0)
            {
                least_common_multiple = M * N / i;
                break;
            }
        }
        else
        {
            least_common_multiple = M * N;
        }
    }

    //// END YOUR CODE HERE ////
    return least_common_multiple;
}
