char alternate_case(unsigned int i, char c)
{
	if (c >= 'a' && c <= 'z')
	{
		if (i % 2 == 0)  // evens: uppercase
			return c - 32;
	}
	else if (c >= 'A' && c <= 'Z')
	{
		if (i % 2 == 1)  // odd: lowercase
			return c + 32;
	}
	return c;
}

int main()
{
	char	str[50] = "Hello. How r You?";

	printf("🧪 TESTING ft_strmapi\n");
	printf("======================\n");
	printf("Returned: %s\n", ft_strmapi(str, &alternate_case));
	return (0);
}
