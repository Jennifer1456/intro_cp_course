bool check_with_monkeys(int A, int B, int C)
{
    bool flag = true;
    /// START YOUR CODE HERE ///
    if (A < B)
    {
        flag = false;
    }
    if (B < C)
    {
        flag = false;
    }

    //// END YOUR CODE HERE ////
    return flag;
}
