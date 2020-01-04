
CREATE TABLE products (
                id INT AUTO_INCREMENT NOT NULL,
                name VARCHAR NOT NULL,
                category VARCHAR NOT NULL,
                nutriscore VARCHAR NOT NULL,
                url VARCHAR NOT NULL,
                store VARCHAR NOT NULL,
                labels VARCHAR NOT NULL,
                barcode VARCHAR NOT NULL,
                PRIMARY KEY (id)
);


CREATE TABLE favorites (
                id INT AUTO_INCREMENT NOT NULL,
                chosen_product_name VARCHAR NOT NULL,
                id_product_subs INT NOT NULL,
                PRIMARY KEY (id)
);


ALTER TABLE favorites ADD CONSTRAINT favorites_products_fk
FOREIGN KEY (id_product_subs)
REFERENCES products (id)
ON DELETE NO ACTION
ON UPDATE NO ACTION;
