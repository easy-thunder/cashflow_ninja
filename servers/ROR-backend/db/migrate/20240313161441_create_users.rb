class CreateUsers < ActiveRecord::Migration[7.0]
  def change
    create_table :users do |t|
      t.string :email, limit: 255
      t.string :password_digest, limit: 255
      t.boolean :is_admin
      t.boolean :can_view_all_accounts
      t.boolean :mfa_enabled
      t.references :family, null: false, foreign_key: true

      t.timestamps
    end
    add_index :users, :email, unique: true
  end
end
