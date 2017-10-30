var gulp = require('gulp'),
    concat = require('gulp-concat'),
    uglify = require('gulp-uglify'),
    rename = require('gulp-rename'),
    sass = require('gulp-sass'),
    sourcemaps = require('gulp-sourcemaps'),
    autoprefixer = require('gulp-autoprefixer'),
    browserSync = require('browser-sync').create();

var DEST = '{{ project_name }}/static/';

gulp.task('scripts', function() {
    return gulp.src([
        'src/js/helpers/*.js',
        'src/js/custom/*.js',
        'src/js/*.js',
      ])
      .pipe(concat('custom.js'))
      .pipe(gulp.dest(DEST+'/js'))
      .pipe(rename({suffix: '.min'}))
      .pipe(uglify())
      .pipe(gulp.dest(DEST+'/js'));
});

gulp.task('sass', function() {
    return gulp.src(['src/scss/*.scss'])
        .pipe(sourcemaps.init())
        .pipe(sass({outputStyle: 'compressed'}).on('error', sass.logError))
        .pipe(autoprefixer('last 2 versions', '> 5%'))
        .pipe(rename({suffix: '.min'}))
        .pipe(sourcemaps.write('.'))
        .pipe(gulp.dest(DEST+'/css'))
        .pipe(browserSync.stream({once: true}));
});

gulp.task('watch', function() {
  // Watch .js files
  gulp.watch('src/js/*.js', ['scripts']);
  gulp.watch('src/js/custom/*.js', ['scripts']);
  gulp.watch('src/js/helper/*.js', ['scripts']);
  // Watch .scss files
  gulp.watch('src/scss/**/*.scss', ['sass']);
});

gulp.task('build', ['sass', 'scripts']);

// Default Task
gulp.task('default', ['build', 'watch']);
