/**
 * @author Victor I. Afolabi
 *
 * A.I. Engineer & Software developer
 * javafolabi@gmail.com
 *
 * Created on 31 January, 2018 @ 3:13 PM.
 * Copyright © 2018. Victor. All rights reserved.
 */

const webpack = require('webpack');

const config = {
  entry: __dirname + '/js/index.jsx',

  output: {
    path: __dirname + '/dist',
    filename: 'bundle.js',
  },

  resolve: {
    extensions: ['.js', '.jsx', '.css']
  },

  module: {
    rules: [
      {
        test: /\.jsx?/,
        exclude: /node_modules/,
        use: 'babel-loader'
      }
    ]
  },

};


module.exports = config;
