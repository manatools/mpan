if(POLICY CMP0048)
	cmake_policy(SET CMP0048 NEW)
endif(POLICY CMP0048)

cmake_minimum_required(VERSION 3.7)

project(mpan VERSION 0.1)

include(GNUInstallDirs)
set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_SOURCE_DIR}/cmake")

find_package(PythonInterp 3.4 REQUIRED)
find_package(Gettext)
execute_process(COMMAND ${PYTHON_EXECUTABLE} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(), end='')" OUTPUT_VARIABLE PYTHON_INSTALL_DIR)
string(REGEX REPLACE "\n$" "" ${PYTHON_INSTALL_DIR} "${PYTHON_INSTALL_DIR}")
execute_process(COMMAND ${PYTHON_EXECUTABLE} -c "import sys; sys.stdout.write('%s.%s' % (sys.version_info.major, sys.version_info.minor))" OUTPUT_VARIABLE PYTHON_MAJOR_DOT_MINOR_VERSION)
message(STATUS "Python install dir is ${PYTHON_INSTALL_DIR}")

option(CHECK_RUNTIME_DEPENDENCIES "Verify the presence of runtime-only dependencies?" ON)

if(CHECK_RUNTIME_DEPENDENCIES)
	include(FindPythonModule)

	# Find the python-manatools module
	find_python_module(manatools REQUIRED)

	# Find yui module
	find_python_module(yui REQUIRED)

	# Find imortlib module
	find_python_module(importlib REQUIRED)

	# Find os module
	find_python_module(os REQUIRED)
	
	find_python_module(glob REQUIRED)
	
	find_python_module(logging REQUIRED)
	
	find_python_module(gettext REQUIRED)

endif(CHECK_RUNTIME_DEPENDENCIES)

set(USE_COMPS "False")

# Set install dirs.
set(CMAKE_INSTALL_BINDIR "${CMAKE_INSTALL_PREFIX}/bin")
set(CMAKE_INSTALL_DATAROOTDIR "${CMAKE_INSTALL_PREFIX}/share")
set(CMAKE_INSTALL_IMAGESROOTDIR "${CMAKE_INSTALL_PREFIX}/share/icons/manatools/images")
set(CMAKE_INSTALL_LOCALEDIR "${CMAKE_INSTALL_DATAROOTDIR}/locale")
set(CMAKE_INSTALL_FULL_SYSCONFDIR "/etc" CACHE PATH "sysconfig directory (default /etc)")

set(CONFIG_FILES_DIR "${CMAKE_INSTALL_FULL_SYSCONFDIR}/mpan")
set(CONFIG_FILES_SUBDIR "${CONFIG_FILES_DIR}/categories.conf.d")

# Build and install translations
 if(GETTEXT_FOUND)
	add_subdirectory(po)
 endif(GETTEXT_FOUND)

# Installing application code
install(PROGRAMS ${CMAKE_SOURCE_DIR}/mpan/mpan DESTINATION ${CMAKE_INSTALL_BINDIR})
install(PROGRAMS ${CMAKE_SOURCE_DIR}/mpan/configreader.py DESTINATION ${PYTHON_INSTALL_DIR})
install(FILES ${CMAKE_SOURCE_DIR}/conf/categories.conf DESTINATION ${CONFIG_FILES_DIR})


# Installing additional configuration files
install(FILES ${CMAKE_SOURCE_DIR}/conf/dnfdragora.conf DESTINATION ${CONFIG_FILES_SUBDIR})
install(FILES ${CMAKE_SOURCE_DIR}/conf/manaproxy.conf DESTINATION ${CONFIG_FILES_SUBDIR})
install(FILES ${CMAKE_SOURCE_DIR}/conf/manadm.conf DESTINATION ${CONFIG_FILES_SUBDIR})
install(FILES ${CMAKE_SOURCE_DIR}/conf/manaadduser.conf DESTINATION ${CONFIG_FILES_SUBDIR})
install(FILES ${CMAKE_SOURCE_DIR}/conf/manauser.conf DESTINATION ${CONFIG_FILES_SUBDIR})
install(FILES ${CMAKE_SOURCE_DIR}/conf/manaservice.conf DESTINATION ${CONFIG_FILES_SUBDIR})
install(FILES ${CMAKE_SOURCE_DIR}/conf/manahost.conf DESTINATION ${CONFIG_FILES_SUBDIR})
install(FILES ${CMAKE_SOURCE_DIR}/conf/manaclock.conf DESTINATION ${CONFIG_FILES_SUBDIR})
install(FILES ${CMAKE_SOURCE_DIR}/conf/manawall.conf DESTINATION ${CONFIG_FILES_SUBDIR})

# Installing icons
install(DIRECTORY ${CMAKE_SOURCE_DIR}/extras/images DESTINATION ${CMAKE_INSTALL_IMAGESROOTDIR} )

# Buils configuration file
file(WRITE ${CMAKE_BINARY_DIR}/mpan.yaml "log_level : debug\nTheme :\n    path : ${CMAKE_INSTALL_IMAGESROOTDIR}\nConfiguration :\n    path : ${CONFIG_FILES_DIR}")
configure_file(${CMAKE_BINARY_DIR}/mpan.yaml ${CONFIG_FILES_DIR} @ONLY)

# install(FILES ${CMAKE_SOURCE_DIR}/extras/mpan.desktop DESTINATION ${CMAKE_INSTALL_DATAROOTDIR}/applications)
