<?php

$password = '123456';

// $hash = password_hash($password, PASSWORD_DEFAULT);

// echo $hash;

$hash = '$2y$10$QbWpiP/.yXjAkS4uWOwloOZ1wWPmYqqT2FYdUn1DhxdheVU82jn4a';

var_dump(password_verify($password, $hash));