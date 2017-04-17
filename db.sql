# Table structure to store crawled sites
CREATE TABLE `sites` (
  `id`      INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
  `url`     VARCHAR(1024)    NOT NULL,
  `title`   VARCHAR(1024)             DEFAULT NULL,
  `updated` TIMESTAMP        NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
)
  ENGINE = InnoDB
  AUTO_INCREMENT = 258
  DEFAULT CHARSET = utf8;