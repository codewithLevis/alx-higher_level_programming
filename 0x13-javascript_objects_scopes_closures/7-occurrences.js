#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const arr = list.filter((n) => {
    return n === searchElement;
  });
  return arr.length;
};
