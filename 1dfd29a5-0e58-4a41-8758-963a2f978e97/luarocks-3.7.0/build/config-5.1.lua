-- LuaRocks configuration

rocks_trees = {
   { name = "user", root = home .. "/.luarocks" };
   { name = "system", root = "/usr/local" };
}
lua_interpreter = "lua5.1";
variables = {
   LUA_DIR = "/usr";
   LUA_BINDIR = "/usr/bin";
}
