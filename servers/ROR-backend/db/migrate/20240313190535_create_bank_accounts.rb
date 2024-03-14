class CreateBankAccounts < ActiveRecord::Migration[7.0]
  def change
    create_table :bank_accounts do |t|
      t.string :account_number
      t.string :account_name
      t.decimal :available_balance, precision: 10, scale: 2
      t.string :institutional_name
      t.decimal :debt, precision: 10, scale: 2

      t.references :user, null: false, foreign_key: true
      t.timestamps
    end
  end
end