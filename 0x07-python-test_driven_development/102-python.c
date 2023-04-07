#include <Python.h>
#include <stdio.h>

/**
 * print_python_string -  function that prints Python strings
 * @p: A PyObject object.
 */
void print_python_string(PyObject *p)
{
	long int len;

	printf("[.] string object info\n");

	if (!PyUnicode_Check(p))
	{
	printf("  [ERROR] Invalid String Object\n");
	return;
	}

	len = PyUnicode_GET_LENGTH(p);

	if (PyUnicode_IS_COMPACT_ASCII(p))
	printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	
	printf("  length: %ld\n", len);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &len));
}
