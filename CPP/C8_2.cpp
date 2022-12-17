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
    if (A > (B + C) || B > (A + C) || C > (A + B))
    {
        flag = true;
    }
    //// END YOUR CODE HERE ////
    return flag;
}
