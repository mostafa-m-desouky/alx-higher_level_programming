#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints python list info
 *
 * @p: PyObject
 * Return: no return
 */
void print_python_list_info(PyObject *p)
{
	long int sz, i;
	PyListObject *ls;
	PyObject *tm;

	sz = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", sz);

	ls = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", ls->allocated);

	for (i = 0; i < sz; i++)
	{
		tm = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(tm)->tp_name);
	}
}
