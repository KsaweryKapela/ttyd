DROP TABLE IF EXISTS 'JPK_HEADER';
DROP TABLE IF EXISTS 'JPK_ENTITY';
DROP TABLE IF EXISTS 'VAT_SALE';
DROP TABLE IF EXISTS 'VAT_PURCHASE';

CREATE TABLE 'JPK_HEADER'
(
    'HEADER_ID' NUMERIC NOT NULL PRIMARY KEY,
    'SEND_TIME' NUMERIC NOT NULL,
    'CREATION_TIME' NUMERIC NOT NULL,
    'DATE_FROM' NUMERIC NOT NULL,
    'DATE_TO' NUMERIC NULL,
    'YEAR_MONTH' NUMERIC NOT NULL
);

CREATE TABLE 'JPK_ENTITY'
(
    'ENTITY_ID' NUMERIC NOT NULL PRIMARY KEY,
    'HEADER_ID' NUMERIC NOT NULL,
    'TAX_ID' TEXT NOT NULL,
    'FIRST_NAME' TEXT NOT NULL,
    'LAST_NAME' TEXT NOT NULL,
    'BIRTH_DATE' NUMERIC NOT NULL,
    'PHONE' NUMERIC NULL,
    CONSTRAINT 'FK_JPK_ENTITY_JPK_HEADER' FOREIGN KEY ('HEADER_ID') REFERENCES 'JPK_HEADER' ('HEADER_ID') ON DELETE No Action ON UPDATE No Action
);

CREATE TABLE 'VAT_SALE'
(
    'SALE_ID' NUMERIC NOT NULL PRIMARY KEY,
    'HEADER_ID' NUMERIC NOT NULL,
    'CONTRACTOR_NUMBER' TEXT NOT NULL,
    'SALES_DOCUMENT' TEXT NOT NULL,
    'ISSUE_DATE' NUMERIC NOT NULL,
    'SALE_DATE' NUMERIC NOT NULL,
    'P_6' NUMERIC NULL,
    'P_8' NUMERIC NULL,
    'P_9' NUMERIC NULL,
    'P_11' NUMERIC NULL,
    'P_13' NUMERIC NULL,
    'P_15' NUMERIC NULL,
    'P_16' NUMERIC NULL,
    'P_19' NUMERIC NULL,
    'P_96' NUMERIC NULL,
    CONSTRAINT 'FK_VAT_SALE_JPK_HEADER' FOREIGN KEY ('HEADER_ID') REFERENCES 'JPK_HEADER' ('HEADER_ID') ON DELETE No Action ON UPDATE No Action
);

CREATE TABLE 'VAT_PURCHASE'
(
    'PURCHASE_ID' NUMERIC NOT NULL PRIMARY KEY,
    'HEADER_ID' NUMERIC NOT NULL,
    'SUPPLIER_NUMBER' TEXT NOT NULL,
    'PURCHASE_DOCUMENT' TEXT NOT NULL,
    'PURCHASE_DATE' NUMERIC NOT NULL,
    'ENTRY_DATE' NUMERIC NOT NULL,
    'P_61' NUMERIC NULL,
    'P_77' NUMERIC NULL,
    'P_78' NUMERIC NULL,
    CONSTRAINT 'FK_VAT_PURCHASE_JPK_HEADER' FOREIGN KEY ('HEADER_ID') REFERENCES 'JPK_HEADER' ('HEADER_ID') ON DELETE No Action ON UPDATE No Action
);