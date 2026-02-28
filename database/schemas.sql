-- Master Tables
create table users (
    uid serial primary key,
    username varchar(50) unique not null,
    passwd_hash text not null,
    role varchar(50) not null,
    created_at timestamp default current_timestamp
);

create table suppliers (
    supp_id serial primary key,
    supp_name varchar(50) not null,
    contact_person varchar(50),
    phone varchar(20) not null,
    address text not null,
    created_at timestamp default current_timestamp
);

create table items (
    item_id serial primary key,
    sku varchar(50) unique not null,
    item_name varchar(50) not null,
    unit varchar(20),
    reorder_level int default 0,
    created_at timestamp default current_timestamp
);

create table warehouses (
    wh_id serial primary key,
    wh_name varchar(50) not null,
    location text not null,
    created_at timestamp default current_timestamp
);
-- ----------------------------------------------------

create table purchase_orders (
    po_id serial primary key,
    supp_id int references suppliers(supp_id),
    created_by int references users(uid),
    order_date timestamp default current_timestamp,
    status varchar(50) default 'pending'
);

create table po_items (
    po_item_id serial primary key,
    po_id int references purchase_orders(po_id) on delete cascade,
    item_id int references items(item_id),
    ordered_qty int not null,
    unit_price numeric(10,2)
);

create table grn (
    grn_id serial primary key,
    po_id int references purchase_orders(po_id),
    supp_id int references suppliers(supp_id),
    received_by int references users(uid),
    received_date timestamp default current_timestamp
);

create table grn_items(
    grn_item_id serial primary key,
    grn_id int references grn(grn_id) on delete cascade,
    item_id int references items(item_id),
    wh_id int references warehouses(wh_id),
    qty_received int not null
);

create table stock_adjust (
    adj_id serial primary key,
    item_id int references items(item_id),
    wh_id int references warehouses(wh_id),
    processed_by int references users(uid),
    qty_adj int not null,
    reason text not null,
    adj_date timestamp default current_timestamp
);

create table stock_moves (
    move_id serial primary key,
    item_id int references items(item_id),
    wh_id int references warehouses(wh_id),
    qty_change int not null,
    move_type varchar(50) not null,
    ref_id int,
    performed_by int references users(uid),
    move_time timestamp default current_timestamp
);

create table item_stock (
    stock_id serial primary key,
    item_id int references items(item_id),
    wh_id int references warehouses(wh_id),
    qty_on_hand int not null default 0,
    last_updated timestamp default current_timestamp,
    unique(item_id, wh_id)
);