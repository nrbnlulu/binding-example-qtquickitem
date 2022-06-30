python3 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
conan config set general.revisions_enabled=1
conan config set general.cmake_generator=Ninja
conan install . -r qt --build=missing --profile=./profiles/linux-x86_64-gcc -if build
source ./build/activate.sh
conan build . -bf build -if build


