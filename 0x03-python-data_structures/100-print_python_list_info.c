#include <object.h>
#include <listobject.h>
#include <Python.h>

/**
* print_python_list_info - C function that prints some
*basic info about Python lists.
* @p: python object pointer
*Return: void
*/

void print_python_list_info(PyObject *p)
{
	PyListObject *list = (PyListObject *) p;
	Py_ssize_t i;
	PyObject *item;

	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < PyList_Size(p); ++i)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, item->ob_type->tp_name);
	}
}
