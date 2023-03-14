#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <stdio.h>

/**
 * print_python_list_info - prints some
 *basic info about Python lists
 * @p: python object.
 */
void print_python_list_info(PyObject *p)
{
	int psize = Py_SIZE(p);
	int j, palloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", psize);
	printf("[*] Allocated = %d\n", palloc);

	j = 0;
	while (j < size)
	{
		printf("Element %d: ", j);
		printf("%s\n", ((PyList_GetItem(p, i))->ob_type)->tp_name);
		i++;
	}
}
