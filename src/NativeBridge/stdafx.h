// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT license.

#pragma once

#if defined( _MSC_VER )
#include "targetver.h"

//
// Exclude rarely-used stuff from Windows headers
//
#define WIN32_LEAN_AND_MEAN             
#define EXPORT_API(ret) extern "C" __declspec(dllexport) ret __stdcall
#define STDCALL __stdcall
#define W(str) L ## str
#define MANAGED_CALLBACK(ret) ret __stdcall
#define MANAGED_CALLBACK_PTR(ret, name) ret (__stdcall *name)
#define CLASS_ALIGN __declspec(align(8))

typedef __int64				CxInt64;
typedef unsigned __int64	CxUInt64;
typedef unsigned char		BYTE;

//
// Windows Header Files:
//
#include <windows.h>

#else // Linux/Mac
// For Unix, ignore __stdcall.
#define STDCALL
#define W(str) str
#define FAILED(Status) ((Status) < 0)
#define MANAGED_CALLBACK(ret) ret
#define MANAGED_CALLBACK_PTR(ret, name) ret ( *name)
#define CLASS_ALIGN __attribute__((aligned(8)))

#ifdef BOOST_NO_CXX11_NULLPTR
#define nullptr 0
#endif //BOOST_NO_CXX11_NULLPTR

typedef long long	CxInt64;
typedef unsigned long long	CxUInt64;
typedef unsigned char	BYTE;

#endif //_MSC_VER

#ifdef BOOST_PYTHON
#include <boost/python.hpp>
#else
#include <pybind11/pybind11.h>
#endif
#include <string>
#include <exception>
#ifdef BOOST_PYTHON
#include <boost/python/numpy.hpp>
#include <boost/python/scope.hpp>
#else
#include <pybind11/numpy.h>
//#include <pybind11/scope.h>
#endif
#include <sysmodule.h>

// #define MEASURE_PERFORMANCE 1

#if defined(MEASURE_PERFORMANCE)

#include <chrono>
#include <functional>
#include <iostream>
#include <sstream>

class StopWatch
{
public:
    typedef std::function<void(const char *)> PrintFunction;

    StopWatch(const char* description, PrintFunction function = nullptr) :
        m_description(description),
        m_printFunction(function)
    {
        m_startTime = std::chrono::high_resolution_clock::now();

        if (m_printFunction == nullptr)
        {
            m_printFunction = [](const char * message) { std::cout << message;  };
        }
    }

    ~StopWatch()
    {
        auto endTime = std::chrono::high_resolution_clock::now();
        
        std::stringstream buffer;
        buffer << m_description << ":" << ((endTime - m_startTime).count() / 1000000) << " msecs" << std::endl;

        m_printFunction(buffer.str().c_str());
    }

private:

    //
    // data members
    //
    std::chrono::steady_clock::time_point m_startTime;
    PrintFunction m_printFunction;
    const char* m_description;
};

#define TOKENPASTE(x, y) x ## y
#define TOKENPASTE2(x, y) TOKENPASTE(x, y)
#define MEASURE_ELAPSED_TIME(description) StopWatch TOKENPASTE2(_stopWatch_, __LINE__)(description)

#else

#define MEASURE_ELAPSED_TIME(description) 

#endif

//
// frequently used namespace aliases
//
#ifdef BOOST_PYTHON
namespace bp = boost::python;
namespace np = boost::python::numpy;
#if !defined(extract_or_cast)
#define extract_or_cast extract
#define has_key_or_contains has_key
#define numpy_array np::ndarray
#endif
#else
namespace bp = pybind11;
//namespace np = pybind11::
#if !defined(extract_or_cast)
#define extract_or_cast cast
#define has_key_or_contains contains
#define numpy_array bp::array
#define numpy_array_bool bp::array_t<bool>
#define numpy_array_int bp::array_t<int>
#define numpy_array_double bp::array_t<double>
#define numpy_array_float bp::array_t<float>
#endif
#endif
