INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_FFT_DECODER fft_decoder)

FIND_PATH(
    FFT_DECODER_INCLUDE_DIRS
    NAMES fft_decoder/api.h
    HINTS $ENV{FFT_DECODER_DIR}/include
        ${PC_FFT_DECODER_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    FFT_DECODER_LIBRARIES
    NAMES gnuradio-fft_decoder
    HINTS $ENV{FFT_DECODER_DIR}/lib
        ${PC_FFT_DECODER_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(FFT_DECODER DEFAULT_MSG FFT_DECODER_LIBRARIES FFT_DECODER_INCLUDE_DIRS)
MARK_AS_ADVANCED(FFT_DECODER_LIBRARIES FFT_DECODER_INCLUDE_DIRS)

