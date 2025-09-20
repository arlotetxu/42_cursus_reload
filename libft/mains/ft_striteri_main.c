void alternate_case(unsigned int i, char *c)
{
	if (*c >= 'a' && *c <= 'z')
	{
		if (i % 2 == 0)  // evens: uppercase
			*c = *c - 32;
	}
	else if (*c >= 'A' && *c <= 'Z')
	{
		if (i % 2 == 1)  // odd: lowercase
			*c = *c + 32;
	}
	//return *c;
}

int main()
{
	char	str[50] = "Hello. How r You?";

	printf("🧪 TESTING ft_strmapi\n");
	printf("======================\n");
	printf("Original string: %s\n", str);
	ft_striteri(str, &alternate_case);
	printf("Modified string: %s\n", str);
	return (0);
}