#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

void print_python_list(PyObject *p) {
    Py_ssize_t size, i;
    const char *type;
    PyListObject *list = (PyListObject *)p;

    if (!list || !PyList_Check(list)) {
        fprintf(stderr, "[ERROR] Invalid List Object\n");
        return;
    }

    size = PyList_Size(p);

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);

    for (i = 0; i < size; i++) {
        type = Py_TYPE(PyList_GetItem(p, i))->tp_name;
        printf("Element %ld: %s\n", i, type);

        if (strcmp(type, "bytes") == 0)
            print_python_bytes(PyList_GetItem(p, i));
        else if (strcmp(type, "float") == 0)
            print_python_float(PyList_GetItem(p, i));
    }
}

void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;
    PyBytesObject *bytes = (PyBytesObject *)p;

    if (!bytes || !PyBytes_Check(bytes)) {
        fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
        return;
    }

    printf("[.] bytes object info\n");
    size = PyBytes_Size(p);
    printf("  size: %ld\n", size);

    printf("  first %ld bytes: ", (size > 10) ? 10 : size);
    for (i = 0; i < size && i < 10; i++)
        printf("%02hhx ", bytes->ob_sval[i]);
    printf("\n");
}

void print_python_float(PyObject *p) {
    char *buffer = NULL;

    if (!p || !PyFloat_Check(p)) {
        fprintf(stderr, "[ERROR] Invalid Float Object\n");
        return;
    }

    printf("[.] float object info\n");

    buffer = PyOS_double_to_string(((PyFloatObject *)p)->ob_fval, 'r', 0,
                                    Py_DTSF_ADD_DOT_0, NULL);
    
    if (buffer) {
        printf("  value: %s\n", buffer);
        PyMem_Free(buffer);
    } else {
        fprintf(stderr, "[ERROR] Failed to convert float to string\n");
    }
}

int main() {
    // Example usage
    Py_Initialize();

    PyObject *list = PyList_New(3);
    PyObject *bytes = PyBytes_FromString("Hello, World!");
    PyObject *flt = PyFloat_FromDouble(3.14);

    PyList_SetItem(list, 0, PyLong_FromLong(42));
    PyList_SetItem(list, 1, bytes);
    PyList_SetItem(list, 2, flt);

    print_python_list(list);

    Py_DECREF(list);
    Py_DECREF(bytes);
    Py_DECREF(flt);

    Py_Finalize();

    return 0;
}
