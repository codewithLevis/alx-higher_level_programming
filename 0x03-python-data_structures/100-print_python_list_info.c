#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <stdio.h>

/**
 * print_python_list_info - C function that prints some
 *basic info about Python lists
 * @p: python object.
 *Return: 0
 */
void print_python_list_info(PyObject *p)
{
	int size = Py_SIZE(p);
	int i, alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);
		printf("%s\n", ((PyList_GetItem(p, i))->ob_type)->tp_name);
	}
}
