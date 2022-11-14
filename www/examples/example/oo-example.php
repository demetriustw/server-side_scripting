<?php

require 'Item.php';
require 'Book.php';

$my_item = new Item();

echo $my_item->code;

$book = new Book();

echo $book->getCode();
