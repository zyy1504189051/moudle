# ************************************************************
# Sequel Pro SQL dump
# Version 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: 127.0.0.1 (MySQL 5.1.73)
# Database: car_ins_account
# Generation Time: 2017-08-16 02:58:53 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table ci_account
# ------------------------------------------------------------

CREATE TABLE `ci_account` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(32) DEFAULT NULL COMMENT '登陆账号',
  `password` varchar(128) NOT NULL,
  `vpn_username` varchar(32) DEFAULT NULL COMMENT 'vpn登陆账号',
  `vpn_password` varchar(128) DEFAULT NULL COMMENT 'vpn登陆密码',
  `ins_company` varchar(16) DEFAULT NULL COMMENT '保险公司编码',
  `login_type` tinyint(4) DEFAULT '0' COMMENT '登陆类型',
  `department_code` varchar(16) DEFAULT NULL COMMENT '报价机构代码',
  `department_name` varchar(32) DEFAULT NULL COMMENT '报价机构名称',
  `seller_code` varchar(16) DEFAULT NULL COMMENT '销售员代码',
  `seller_name` varchar(32) DEFAULT NULL COMMENT '销售员姓名',
  `area` varchar(16) DEFAULT NULL COMMENT '地域',
  `proxy` varchar(32) DEFAULT NULL COMMENT '代理服务器',
  `is_bank` tinyint(2) DEFAULT '0' COMMENT '是否银行1是-1否',
  `cookies` varchar(2000) DEFAULT NULL,
  `pre_url` varchar(2000) DEFAULT '' COMMENT '预请求地址，仅用于太保网销',
  `pre_verify` tinyint(4) DEFAULT '-1' COMMENT '是否处罚预核保，仅用于太保网销',
  `created` datetime DEFAULT NULL,
  `updated` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_ci_account_username` (`username`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table ci_agent
# ------------------------------------------------------------

CREATE TABLE `ci_agent` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `partner_id` int(11) DEFAULT NULL,
  `agent_code` varchar(32) DEFAULT NULL COMMENT '代理人编码',
  `agent_name` varchar(32) DEFAULT NULL COMMENT '代理人名称',
  `created` datetime DEFAULT NULL,
  `updated` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table ci_branch
# ------------------------------------------------------------

CREATE TABLE `ci_branch` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `partner_id` int(11) DEFAULT NULL,
  `agent_id` int(11) DEFAULT NULL,
  `branch_code` varchar(32) DEFAULT NULL COMMENT '代理网点编码',
  `branch_name` varchar(32) DEFAULT NULL COMMENT '代理网点名称',
  `created` datetime DEFAULT NULL,
  `updated` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table ci_partner
# ------------------------------------------------------------

CREATE TABLE `ci_partner` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `account_id` int(11) DEFAULT NULL,
  `partner_code` varchar(16) DEFAULT NULL COMMENT '合作网点代码',
  `partner_name` varchar(16) DEFAULT NULL COMMENT '合作网点名称',
  `business_code` varchar(16) DEFAULT NULL COMMENT '合作渠道代码',
  `business_detail_code` varchar(16) DEFAULT NULL COMMENT '合作渠道细分代码2',
  `channel_code` varchar(16) DEFAULT NULL COMMENT '合作渠道代码',
  `channel_detail_code` varchar(16) DEFAULT NULL COMMENT '合作渠道细分代码2',
  `created` datetime DEFAULT NULL,
  `updated` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table ci_protocol
# ------------------------------------------------------------

CREATE TABLE `ci_protocol` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `partner_id` int(11) DEFAULT NULL,
  `agent_id` int(11) DEFAULT NULL,
  `branch_id` int(11) DEFAULT NULL,
  `protocol_code` varchar(32) DEFAULT NULL COMMENT '协议编码',
  `protocol_name` varchar(32) DEFAULT NULL COMMENT '协议名称',
  `protocol_sub_code` varchar(32) DEFAULT NULL COMMENT '协议子编码',
  `product` varchar(1000) DEFAULT NULL COMMENT '产品描述',
  `created` datetime DEFAULT NULL,
  `updated` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;




/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
