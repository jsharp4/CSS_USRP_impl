# Install script for directory: /home/jsarp4/Documents/gnu_radio_flowcharts/CSS_USRP_impl/gr-fft_decoder

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/fft_decoder" TYPE FILE FILES "/home/jsarp4/Documents/gnu_radio_flowcharts/CSS_USRP_impl/gr-fft_decoder/cmake/Modules/fft_decoderConfig.cmake")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/home/jsarp4/Documents/gnu_radio_flowcharts/CSS_USRP_impl/gr-fft_decoder/python/include/fft_decoder/cmake_install.cmake")
  include("/home/jsarp4/Documents/gnu_radio_flowcharts/CSS_USRP_impl/gr-fft_decoder/python/lib/cmake_install.cmake")
  include("/home/jsarp4/Documents/gnu_radio_flowcharts/CSS_USRP_impl/gr-fft_decoder/python/swig/cmake_install.cmake")
  include("/home/jsarp4/Documents/gnu_radio_flowcharts/CSS_USRP_impl/gr-fft_decoder/python/python/cmake_install.cmake")
  include("/home/jsarp4/Documents/gnu_radio_flowcharts/CSS_USRP_impl/gr-fft_decoder/python/grc/cmake_install.cmake")
  include("/home/jsarp4/Documents/gnu_radio_flowcharts/CSS_USRP_impl/gr-fft_decoder/python/apps/cmake_install.cmake")
  include("/home/jsarp4/Documents/gnu_radio_flowcharts/CSS_USRP_impl/gr-fft_decoder/python/docs/cmake_install.cmake")

endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/home/jsarp4/Documents/gnu_radio_flowcharts/CSS_USRP_impl/gr-fft_decoder/python/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
