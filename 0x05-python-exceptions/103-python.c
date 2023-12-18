#include <Python.h>

void print_list_info(PyListObject *list);
void print_bytes_info(PyBytesObject *bytes);
void print_float_info(PyFloatObject *flt);

void print_python_object_info(PyObject *p) {
    if (p == NULL) {
        fprintf(stderr, "[ERROR] Invalid Object\n");
        return;
    }

    if (PyList_Check(p)) {
        print_list_info((PyListObject *)p);
    } else if (PyBytes_Check(p)) {
        print_bytes_info((PyBytesObject *)p);
    } else if (PyFloat_Check(p)) {
        print_float_info((PyFloatObject *)p);
    } else {
        fprintf(stderr, "[ERROR] Unknown Object Type\n");
    }
}

void print_list_info(PyListObject *list) {
    Py_ssize_t size = PyList_Size((PyObject *)list);
    Py_ssize_t alloc = list->allocated;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", alloc);

    for (Py_ssize_t i = 0; i < size; i++) {
        PyObject *item = PyList_GetItem((PyObject *)list, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
        print_python_object_info(item);
    }
}

void print_bytes_info(PyBytesObject *bytes) {
    Py_ssize_t size = PyBytes_Size((PyObject *)bytes);

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", size);
    
    if (size > 0) {
        printf("  trying string: %s\n", bytes->ob_sval);
        printf("  first %ld bytes: ", (size > 10) ? 10 : size);
        for (Py_ssize_t i = 0; i < size && i < 10; i++) {
            printf("%02hhx ", bytes->ob_sval[i]);
        }
        printf("\n");
    }
}

void print_float_info(PyFloatObject *flt) {
    printf("[.] float object info\n");
    printf("  value: %f\n", flt->ob_fval);
}

int main() {
    // Example usage
    PyObject *list = PyList_New(3);
    PyObject *bytes = PyBytes_FromString("Hello, World!");
    PyObject *flt = PyFloat_FromDouble(3.14);

    PyList_SetItem(list, 0, PyLong_FromLong(42));
    PyList_SetItem(list, 1, bytes);
    PyList_SetItem(list, 2, flt);

    print_python_object_info(list);
    print_python_object_info(bytes);
    print_python_object_info(flt);

    Py_DECREF(list);
    Py_DECREF(bytes);
    Py_DECREF(flt);

    return 0;
}
