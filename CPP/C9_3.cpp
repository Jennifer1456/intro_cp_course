int lottery_function(bool reset = false)
{
    int pick(0);
    /// START YOUR CODE HERE ///
    static int picked[42] = {};
    static int count = 0;

    if (reset)
    {
        count = 0;
        for (int i = 0; i < 42; i++)
        {
            picked[i] = 0;
        }
    }
    else
    {
        bool unique = false;

        if (count >= 42)
        {
            return 0;
        }

        while (!unique)
        {
            unique = true;
            pick = rand() % 42 + 1;

            for (int i = 0; i < count; i++)
            {
                if (picked[i] == pick)
                {
                    unique = false;
                    break;
                }
            }
        }
        picked[count] = pick;
        count++;
    }
    //// END YOUR CODE HERE ////
    return pick;
}
