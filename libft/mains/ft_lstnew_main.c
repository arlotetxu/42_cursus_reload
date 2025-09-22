int main(void)
{
	// --- Ejemplo 1: Crear un nodo con una cadena de texto ---
	char	*mi_texto = "Hola desde un nodo";
	t_list	*nodo1;

	// Llamamos a tu función para crear el nodo
	nodo1 = ft_lstnew(mi_texto);

	// Comprobamos si el nodo se creó correctamente
	if (nodo1)
	{
		printf("--- Nodo 1 (Texto) ---\n");
		printf("Nodo creado correctamente en la direccion: %p\n", (void *)nodo1);
		// Para imprimir el contenido, hacemos un cast de void* a char*
		printf("Contenido del nodo: \"%s\"\n", (char *)nodo1->content);
		printf("El puntero 'next' apunta a: %p\n", (void *)nodo1->next);

		// Liberamos la memoria del nodo (no del contenido, porque es un literal)
		free(nodo1);
	}
	else
		printf("Error: No se pudo crear el nodo 1.\n");
	printf("\n--------------------------\n\n");
	return (0);
}
