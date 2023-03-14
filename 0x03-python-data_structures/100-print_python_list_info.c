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
	long int size = PyList_Size(p);
	int i;

	printf("[*] Size of the Python List = %ld\n", size);

	PyListObject *obj = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", obj->allocated);

	i = 0;

	while(i < size)
	{
		printf("Element %i: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
		i++;
	}	
}
