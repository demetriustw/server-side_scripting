<?php

setcookie('example', 'hello', time() + 60 * 60 * 24 * 2);

echo 'Cookie set.';